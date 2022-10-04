validate = False
#validate_rgb: deve garantir que cada valor informado esteja entre [0 e 255], retornando True ou False
def validate_rgb(value):
        if 0 <= int(value) <= 255:
                value = True 
        else: 
                value = False
        return value                


def rgb2hex(r, g, b):
        r = int(r)
        g = int(g)
        b = int(b)
        return ('#{:02x}{:02x}{:02x}').format(r, g, b).upper()
      

while validate != True:
    rgb_str = input()
    r, g, b = rgb_str.split(' ')
    validate = validate_rgb(r) and validate_rgb(g) and validate_rgb(b)

hex = rgb2hex(r, g, b)

print('A cor {} em hex é {}'.format((r,g,b), (hex)))

#DC143C