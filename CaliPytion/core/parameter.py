import sdRDM

from typing import Optional
from pydantic import Field, PrivateAttr
from sdRDM.base.utils import forge_signature, IDGenerator


@forge_signature
class Parameter(sdRDM.DataModel):
    """"""

    id: Optional[str] = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("parameterINDEX"),
        xml="@id",
    )

    name: Optional[str] = Field(
        default=None,
        description="Name of the parameter",
    )

    value: Optional[float] = Field(
        default=None,
        description="Value of the parameter",
    )

    __repo__: Optional[str] = PrivateAttr(
        default="https://github.com/FAIRChemistry/CaliPytion.git"
    )
    __commit__: Optional[str] = PrivateAttr(
        default="7cf6bf6af8bc7b1907348433652a23ac8b986360"
    )
