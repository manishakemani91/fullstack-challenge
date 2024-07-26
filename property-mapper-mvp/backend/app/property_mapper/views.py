from loguru import logger
from fastapi import Depends, APIRouter, HTTPException, Request
from sqlalchemy.orm import Session
from app.core.db.session import get_db
from sqlalchemy.ext.asyncio import AsyncSession
from app.property_mapper.models import Property
from sqlalchemy import select, String

router = APIRouter()

@router.get("/autocomplete")
async def autocomplete(
    request: Request,
    query: str = "",
    field: str = "full_address",
    page: int = 1,
    page_size: int = 20,
    db: Session = Depends(get_db),
):
    if field not in [
        "full_address",
        "class_description",
        "estimated_market_value",
        "bldg_use",
        "building_sq_ft",
    ]:
        raise HTTPException(status_code=400, detail="Invalid field")
    
    result = []
    column_attr = getattr(Property, field)
    
    try:
    # Checking if the query is a valid integer or float when field is numeric
        if field in ["estimated_market_value", "building_sq_ft"]:
            
            result = db.query(
                Property.id,
                Property.full_address,
                Property.class_description,
                Property.estimated_market_value,
                Property.bldg_use,
                Property.building_sq_ft,
                Property.latitude,
                Property.longitude
            ).filter(
                column_attr.cast(String).ilike(f"%{query}%")
            ).limit(page_size + 1).offset((page - 1) * page_size).all()
        else:
            result = db.query(Property.id, Property.full_address, Property.class_description, Property.estimated_market_value, Property.bldg_use, Property.building_sq_ft, Property.latitude, Property.longitude)\
                .filter(column_attr.ilike(f"%{query}%"))\
                .limit(page_size + 1)\
                .offset((page - 1) * page_size)\
                .all()

        has_more = len(result) > page_size

        # Remove the extra record used to check for more results
        if has_more:
            result = result[:-1]

        autocomplete_results = [{
            "id": row.id,
            "full_address": row.full_address,
            "class_description": row.class_description,
            "estimated_market_value": row.estimated_market_value,
            "bldg_use": row.bldg_use,
            "building_sq_ft": row.building_sq_ft,
            "latitude": row.latitude,
            "longitude": row.longitude
        } for row in result]

        return {
            "results": autocomplete_results,
            "hasMore": has_more
        }

        #return autocomplete_results

    except Exception as e:
        logger.error('error occured while fetching list: ',e)
        raise HTTPException(status_code=500, detail=str(e))
