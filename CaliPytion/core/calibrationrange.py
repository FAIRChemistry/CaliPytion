import sdRDM

from typing import Optional
from pydantic import Field, PrivateAttr
from sdRDM.base.utils import forge_signature, IDGenerator


@forge_signature
class CalibrationRange(sdRDM.DataModel):
    """"""

    id: Optional[str] = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("calibrationrangeINDEX"),
        xml="@id",
    )

    conc_lower: Optional[float] = Field(
        default=None,
        description="Lower concentration bound of the model",
    )

    conc_upper: Optional[float] = Field(
        default=None,
        description="Upper concentration bound of the model",
    )

    signal_lower: Optional[float] = Field(
        default=None,
        description="Lower signal bound of the model",
    )

    signal_upper: Optional[float] = Field(
        default=None,
        description="Upper signal bound of the model",
    )
    __repo__: Optional[str] = PrivateAttr(
        default="https://github.com/FAIRChemistry/CaliPytion"
    )
    __commit__: Optional[str] = PrivateAttr(
        default="d456bfc4a46b88058ef3ad49c77d60fd366af14f"
    )
