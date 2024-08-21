# utilities/color_utils.py

def rgb_to_luminance(rgb):
    r, g, b = rgb
    r, g, b = [x / 255.0 for x in (r, g, b)]
    r, g, b = [x / 12.92 if x <= 0.03928 else ((x + 0.055) / 1.055) ** 2.4 for x in (r, g, b)]
    return 0.2126 * r + 0.7152 * g + 0.0722 * b

def contrast_ratio(lum1, lum2):
    if lum1 > lum2:
        return (lum1 + 0.05) / (lum2 + 0.05)
    else:
        return (lum2 + 0.05) / (lum1 + 0.05)

def adjust_color(rgb, target_luminance, tolerance=0.1):
    r, g, b = rgb
    current_luminance = rgb_to_luminance(rgb)
    adjustment_factor = target_luminance / current_luminance

    def adjust_channel(channel):
        return min(max(int(channel * adjustment_factor), 0), 255)

    return (adjust_channel(r), adjust_channel(g), adjust_channel(b))

def ensure_contrast(color1, color2, target_contrast=4.5):
    lum1 = rgb_to_luminance(color1)
    lum2 = rgb_to_luminance(color2)

    if contrast_ratio(lum1, lum2) < target_contrast:
        target_luminance = (lum1 + lum2) / 2
        color1 = adjust_color(color1, target_luminance)
        color2 = adjust_color(color2, target_luminance)

    return color1, color2
