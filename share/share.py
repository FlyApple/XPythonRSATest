# encoding: utf-8

import array;

# bytes to hex string text
def bytes2hex_text(buffer, delim = ",", line = True) :
    result = "";
    n = 0;
    for i in range(0, len(buffer)) :
        #
        result += format("%02X"%buffer[i]);
        if len(buffer) > i + 1 :
            result += delim;
        #
        if line :
            n += 1;
            if n >= 0x10 :
                result += "\n";
                n = 0;
    #
    return result;
    #return delim.join(format("%02X"%x) for x in buffer);

# big integer to hex string text
def integer2hex_text(value, length, order = "little", delim = ",", line = True) :
    return bytes2hex_text(int.to_bytes(value, length, byteorder = order), delim, line);

