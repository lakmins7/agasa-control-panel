import json
import socket
# import RPi.GPIO as GPIO
import time
# import spidev

#############################################################
######### For mapping the JS response to bit values #########
#############################################################

def to_bitval(field, value, bitmap):
    if field in bitmap:
        bm = bitmap[field]
        if str(value) in bm:
            return bm[str(value)]
        if isinstance(value, bool):
            return bm["true"] if value else bm["false"]
        if isinstance(value, int) or isinstance(value, float):
            return bm.get(str(int(value)), str(value))
    return str(value)

def bitValueConversionAGASAv1(default_path, bitmap_path, request_body: dict, channels_range=(1,32)):
    with open(default_path) as f:
        default_cfg = json.load(f)
    with open(bitmap_path) as f:
        bitmap = json.load(f)
    # Build merged channel list (1..16)
    user_channels = {c["id"]: c for c in request_body.get("channels", [])}
    default_channels = {c["id"]: c for c in default_cfg["channels"]}
    all_ids = sorted(set(default_channels.keys()) | set(user_channels.keys()))
    # Filter by channels_range
    all_ids = [cid for cid in all_ids if channels_range[0] <= cid <= channels_range[1]]
    merged = []
    for cid in all_ids:
        ch = user_channels.get(cid, default_channels[cid])
        merged.append(ch)
    
    bit_channels = []
    for ch in merged:
        bit_ch = {"id": ch["id"]}
        for k, v in ch.items():
            if k == "id":
                continue
            if k == "threshold":
                # Zero-padded 10-bit binary
                threshold_val = int((v - default_cfg["vcm_dac"]["din"]) / 3.3 * 1023)
                bit_ch["threshold"] = format(threshold_val, '010b')
            else:
                bit_ch[k] = to_bitval(k, v, bitmap)
        bit_channels.append(bit_ch)

    return bit_channels

def bitValueConversionAGASAv2(default_path, bitmap_path, request_body: dict):
    with open(default_path) as f:
        default_cfg = json.load(f)
    with open(bitmap_path) as f:
        bitmap = json.load(f)
    # Build merged channel list (1..16)
    user_channels = {c["id"]: c for c in request_body.get("channels", [])}
    default_channels = {c["id"]: c for c in default_cfg["channels"]}
    all_ids = sorted(set(default_channels.keys()) | set(user_channels.keys()))
    merged = []
    for cid in all_ids:
        ch = user_channels.get(cid, default_channels[cid])
        merged.append(ch)
    
    bit_channels = []
    for ch in merged:
        bit_ch = {"id": ch["id"]}
        for k, v in ch.items():
            if k == "id":
                continue
            if k == "threshold":
                # Zero-padded 10-bit binary
                threshold_val = int((v - default_cfg["vcm_dac"]["din"]) / 3.3 * 1023)
                bit_ch["threshold"] = format(threshold_val, '010b')
            else:
                bit_ch[k] = to_bitval(k, v, bitmap)
        bit_channels.append(bit_ch)

    return bit_channels

def bitValueConversionAGASAv3(default_path, bitmap_path, request_body: dict):
    with open(default_path) as f:
        default_cfg = json.load(f)
    with open(bitmap_path) as f:
        bitmap = json.load(f)
    # Build merged channel list (1..16)
    user_channels = {c["id"]: c for c in request_body.get("channels", [])}
    default_channels = {c["id"]: c for c in default_cfg["channels"]}
    all_ids = sorted(set(default_channels.keys()) | set(user_channels.keys()))
    merged = []
    for cid in all_ids:
        ch = user_channels.get(cid, default_channels[cid])
        merged.append(ch)
    
    bit_channels = []
    for ch in merged:
        bit_ch = {"id": ch["id"]}
        for k, v in ch.items():
            if k == "id":
                continue
            if k == "threshold":
                # Zero-padded 10-bit binary
                threshold_val = int((v+1.8)/ 3.6 * 1023)
                bit_ch["threshold"] = format(threshold_val, '010b')
            else:
                bit_ch[k] = to_bitval(k, v, bitmap)
        bit_channels.append(bit_ch)

    return bit_channels


def createAGASAv1ConfigBits(default_path, channels, debug=False):
    with open(default_path) as f:
        default_cfg = json.load(f)
    # Create the full bitmap
    bit_string = default_cfg["vcm_dac"]["nc"] 
    bit_string += format(int(default_cfg["vcm_dac"]["din"] / -3.3 * 1024),'010b')

    for ch in channels:
        # The first bit for each channel should be "0" ? Because of NC
        if ch["id"] == 32 or ch["id"] == 64:
            bit_string += "1"
        else:
            bit_string += "0"
        bit_string += ch["polarity"]
        bit_string += ch["output"]
        bit_string += ch["testpulse"]
        bit_string += ch["threshold"]
        bit_string += ch["shp_res"]
        bit_string += ch["shp_cap"]
        bit_string += ch["pzc_res"]
        bit_string += ch["pzc_cap"]
        bit_string += ch["csa_res"]
        bit_string += ch["csa_cap"]

        # Always add one extra channel with the default AGASA v2 config
        # if ch["id"] == 16:
        #     # Only the last channel, the first bit should be 1 for PAD_BUF_EN
        #     bit_string += "11001111111111100000100000100000"
        # else:
        #     bit_string += "01001111111111100000100000100000"

    if debug:
        chunks = [bit_string[i:i+8] for i in range(0, len(bit_string), 8)]
        for x in chunks:
            print(f"Hex: {hex(int(x, 2))}, Bits: {x}")
            # print(hex(int(x, 2)))
        print("Length of bit string: ", len(chunks))

    return bit_string

def createAGASAv2ConfigBits(default_path, channels, debug=False):
    with open(default_path) as f:
        default_cfg = json.load(f)
    # Create the full bitmap
    bit_string = default_cfg["vcm_dac"]["nc"] 
    bit_string += format(int(default_cfg["vcm_dac"]["din"] / -3.3 * 1024),'010b')

    for ch in channels:
        # The first bit for each channel should be "0" ? Because of NC
        if ch["id"] == 16:
            bit_string += "1"
        else:
            bit_string += "0"
        bit_string += ch["polarity"]
        bit_string += ch["output"]
        bit_string += ch["testpulse"]
        bit_string += ch["threshold"]
        bit_string += ch["shp_res"]
        bit_string += ch["shp_cap"]
        bit_string += ch["pzc_res"]
        bit_string += ch["pzc_cap"]
        bit_string += ch["csa_res"]
        bit_string += ch["csa_cap"]

        # Always add one extra channel with the default AGASA v2 config
        # if ch["id"] == 16:
        #     # Only the last channel, the first bit should be 1 for PAD_BUF_EN
        #     bit_string += "11001111111111100000100000100000"
        # else:
        #     bit_string += "01001111111111100000100000100000"

    if debug:
        chunks = [bit_string[i:i+8] for i in range(0, len(bit_string), 8)]
        for x in chunks:
            print(f"Hex: {hex(int(x, 2))}, Bits: {x}")
            # print(hex(int(x, 2)))
        print("Length of bit string: ", len(chunks))

    return bit_string

def createAGASAv3ConfigBits(default_path, channels, debug=False):
    with open(default_path) as f:
        default_cfg = json.load(f)
    bit_string = ""

    for ch in channels:
        bit_string += "0"
        bit_string += ch["csa_res"]
        bit_string += ch["csa_cap"]
        bit_string += "0"
        bit_string += ch["shp_res"]
        bit_string += ch["shp_cap"]
        bit_string += "0"
        bit_string += ch["pzc_res"]
        bit_string += ch["pzc_cap"]
        bit_string += "000"
        bit_string += ch["testpulse"]
        bit_string += ch["polarity"]
        bit_string += ch["output"]
        bit_string += ch["threshold"]

    if debug:
        chunks = [bit_string[i:i+8] for i in range(0, len(bit_string), 8)]
        for x in chunks:
            print(f"Hex: {hex(int(x, 2))}, Bits: {x}")
            # print(hex(int(x, 2)))
        print("Length of bit string: ", len(chunks))

    return bit_string

def createAGASAv3ConfigBits1SPI8(default_path, channels, filename):
    with open(default_path) as f:
        default_cfg = json.load(f)
    bit_string = ""

    for ch in channels:
        bit_string += "0"
        bit_string += ch["csa_res"]
        bit_string += ch["csa_cap"]
        bit_string += "0"
        bit_string += ch["shp_res"]
        bit_string += ch["shp_cap"]
        bit_string += "0"
        bit_string += ch["pzc_res"]
        bit_string += ch["pzc_cap"]
        bit_string += "000"
        bit_string += ch["testpulse"]
        bit_string += ch["polarity"]
        bit_string += ch["output"]
        bit_string += ch["threshold"]

    with open(filename, 'w') as out_f:
        chunks = [bit_string[i:i+8] for i in range(0, len(bit_string), 8)]
        for x in chunks:
            out_f.write(f"0x{int(x, 2):02X}\n")

##############################################################
######### For writing using SPI using a Raspberry Pi #########
##############################################################

def init_spi(SPI_BUS, SPI_DEVICE, MAX_SPEED_HZ, SPI_MODE):
    """Initialize SPI using spidev"""
    spi = spidev.SpiDev()
    spi.open(SPI_BUS, SPI_DEVICE)  # Open SPI bus 0, device (CS) 0
    spi.max_speed_hz = MAX_SPEED_HZ  # Set to 1.25 MHz
    spi.mode = SPI_MODE  # SPI mode 0
    # spi.cshigh = False # Chip Select active low
    spi.bits_per_word = 8 # 8 bits per word
    return spi

def write_spi(SPI_BUS, SPI_DEVICE, MAX_SPEED_HZ, SPI_MODE, bit_string):
    spi = init_spi(SPI_BUS, SPI_DEVICE, MAX_SPEED_HZ, SPI_MODE)
    """Write bit string to DUT via hardware SPI at 1.25 MHz
    
    Args:
        bit_string (str): String of '0' and '1' characters to write
    """
    try:
        # Convert bit string to bytes
        # Pack bits into bytes (8 bits per byte)
        bytes_to_send = []
        for i in range(0, len(bit_string), 8):
            byte_bits = bit_string[i:i+8]
            # Pad with zeros if less than 8 bits
            byte_bits = byte_bits.ljust(8, '0')
            byte_val = int(byte_bits, 2)
            bytes_to_send.append(byte_val)
        # Send bytes via SPI
        hexbits = [hex(b) for b in bytes_to_send]
        # print("Length of the bytes: ", len(bytes_to_send))
        spi.xfer2(bytes_to_send)
        
    except Exception as e:
        print(f"SPI write error: {e}")
        raise

######################################################
######### For sending bit values to the FPGA #########
######################################################

def send_to_fpga(bit_string, fpga_ip, fpga_port):
    # Convert bit string (e.g., '11001100') to bytes
    # If your bit_string is a string of '0' and '1', convert to int, then to bytes
    byte_data = int(bit_string, 2).to_bytes((len(bit_string) + 7) // 8, byteorder='big')

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((fpga_ip, fpga_port))
        s.sendall(byte_data)
        # Optionally receive a response
        # response = s.recv(1024)
        # print('Received', response)