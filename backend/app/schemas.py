from pydantic import BaseModel, ConfigDict, Field

class PredictRequest(BaseModel):
    model_config = ConfigDict(extra="forbid") # what should happen to fields we did not ask for? ("ignore", "allow", or "forbid"?)

    # consider what type each one should be - int, float or bool?
    # ge = "greater than or equal", le = "less than or equal" 0 - what do you think these mean?
    danceability: float = Field(ge=0.0, le=1.0)
    energy: float = Field(ge=0.0, le=1.0) # energy should be a value from what to what?
    key: int = Field(ge=-1, le=11, description="Pitch class 0-11; -1 if undetected.") 
    loudness: float = Field(ge=-60.0, le=5.0, description="Decibels.")
    mode: int = Field(ge=0, le=1, description="1 major, 0 minor.")
    speechiness: float = Field(ge=0.0, le=1.0)
    acousticness: float = Field(ge=0.0, le=1.0)
    instrumentalness: float = Field(ge=0.0, le=1.0)
    liveness: float = Field(ge=0.0, le=1.0)
    valence: float = Field(ge=0.0, le=1.0)
    tempo: float = Field(ge=0.0, le=250.0, description="Beats per minute.") # API allows up to 250 BPM
    time_signature: int = Field(ge=0, le=7)
    duration_ms: int = Field(gt=0, le=6_000_000)
    popularity: int = Field(ge=0, le=100)
    explicit: bool