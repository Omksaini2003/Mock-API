from pydantic import BaseModel
from typing import List, Dict, Any, Optional


class PatientInformation(BaseModel):
    dob: str


class DataSection(BaseModel):
    ECG: List[Any]  # raw ECG rows (usually list of lists or empty list)


class DataFormatSection(BaseModel):
    ECG: List[str]  # column names


class PredictRequest(BaseModel):
    DeviceAcquisitionDate: str
    Measurements: Dict[str, Any]     # empty {} allowed
    DeviceID: str
    Data: DataSection
    Gender: str
    Height: int
    Weight: int
    AcquisitionTime: str
    DeviceAcquisitionTime: str
    PatientInformation: PatientInformation
    AcquisitionDevice: str
    AcquisitionDate: str
    Checksum: str
    PatientID: str
    DataFormat: DataFormatSection
    DataType: str
    DiagnosisCodes: List[Any]
    Diagnosis: List[Any]
    RecordID: str
    Age: str
