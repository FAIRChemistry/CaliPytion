from typing import Optional
from pydantic import PrivateAttr
from sdRDM.base.listplus import ListPlus
from pydantic import Field
from typing import List
from .series import Series
from .standardcurve import StandardCurve


class HPLCStandardCurve(StandardCurve):

    peak_area: List[Series] = Field(
        description="Measured peak area, corresponding to the applied concentration.",
        default_factory=ListPlus,
    )

    __repo__: Optional[str] = PrivateAttr(
        default="git://github.com/FAIRChemistry/datamodel_calibration.git"
    )
    __commit__: Optional[str] = PrivateAttr(
        default="f6d13a0ec49b8e54167c7cf0705ac1ca2f68b325"
    )

    def add_to_peak_area(
        self,
        values: List[float] = ListPlus(),
    ) -> None:
        """
        Adds an instance of 'Series' to the attribute 'peak_area'.

        Args:
            values (List[float]): Series representing an array of values.
        """

        self.peak_area.append(
            Series(
                values=values,
            )
        )
