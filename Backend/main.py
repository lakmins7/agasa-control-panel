from fastapi import FastAPI
from datetime import datetime
import json
from pathlib import Path
import subprocess
from fastapi.responses import JSONResponse
from helpers.frontEndHelpers import ChannelConfigRequest
from helpers.backEndHelpers import bitValueConversionAGASAv3 as bitValueConversion
from helpers.backEndHelpers import createAGASAv3ConfigBits1SPI8 as createConfigBits

###############################################################
# Define paths for default config and bitmap
default_path = Path("config/general/default_AGASAv3_config.json")
bitmap_path = Path("config/general/AGASAv3_spi_bitmap.json")

# Define where to save JSON files
SAVE_DIR = Path("config/configs_{}".format(datetime.now().strftime("%Y%m%d")))
SAVE_DIR.mkdir(exist_ok=True)
###############################################################

app = FastAPI()

@app.post("/api/channels/config")
async def apply_config(request: ChannelConfigRequest):
    try:
        # Create filename with timestamp
        filename = SAVE_DIR / f"config_{datetime.now():%Y%m%d_%H%M%S}.prm"

        # Save the full request (with channels array) to JSON file
        with open(filename, "w") as f:
            json.dump(request.dict(), f, indent=4)

        # Convert to bit values
        bit_channels = bitValueConversion(default_path, bitmap_path, request.dict())
        createConfigBits(default_path, bit_channels, filename)

        # Write to device
        subprocess.run("<path-to-asagi-controller> <HUL-IP-address> {0}".format(filename), shell=True, check=True)

        return JSONResponse(content={
            "message": f"Successfully saved config to {SAVE_DIR}/{filename.name}",
            "bit_values": {"channels": bit_channels}
        })
    except Exception as e:
        return JSONResponse(content={"message": f"Error saving config: {e}"}, status_code=500)
