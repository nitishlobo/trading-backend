"""Defines base schema settings for trading schemas."""
from pydantic import BaseModel


class TradingBase(BaseModel):  # pylint: disable=too-few-public-methods
    """Base class for trading schema classes."""

    class Config:  # pylint: disable=too-few-public-methods
        """Class config."""

        # Allows having field as class types
        arbitrary_types_allowed = True
        # Enables validation on field after class construction
        validate_assignment = True
