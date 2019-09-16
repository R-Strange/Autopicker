from dataclasses import dataclass, field
from obspy import UTCDateTime
from typing import Dict


@dataclass()
class SacDataClass:
    source_name: str = field(metadata={"description": "name of the source sac file"})
    network: str = field(metadata={"description": "the IRIS code for the recording network", "example": "YW"})
    station: str = field(metadata={"description": "the IRIS code for the recording station", "example": "NAB1"})
    location: str = field(metadata={"description": "Location information for the recording station"})
    channel: str = field(metadata={
        "description": "the trace's recording channel. Traces typically come in triples: \n"
                       " horizontal (N->S), lateral (E->W) and vertical(Z->-Z) to capture X, Y and Z movement.",
        "example": "HHE"})
    start_time: UTCDateTime = field(metadata={"format": "YYYY-MM-DDTHH:mm:ss:uuuuuuZ",
                                              "example": "2011-08-29T00:23:00.330000Z",
                                              "description": "time and date of the beginning of the trace"})
    end_time: UTCDateTime = field(metadata={"format": "YYYY-MM-DDTHH:mm:ss:uuuuuuZ",
                                           "example": "2011-08-29T00:23:00.330000Z",
                                           "description": "time and date of the end of the trace"})
    sampling_rate: float = field(metadata={"units:": "Hz",
                                           "description": "number of datapoints per second, i.e. frequency"})
    delta: float = field(metadata={"units": "seconds", "description": "time between each datapoint"})
    number_of_points: int = field(metadata={"description": "number of datapoints in the trace"})
    scale_factor: float = field(default=1.0, metadata={"description": "the scale factor that the amplitudes are multiplied by. Default is 1.0"})
    sac_header: Dict = field(metadata={"description": "the internal header information for the "})