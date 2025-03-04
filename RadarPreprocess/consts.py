negative_scale = [(205, 192, 159), (0, 143, 0), (0, 187, 144), (0, 251, 144),
                  (50, 0, 150), (0, 128, 255), (0, 224, 255)]
positive_scale = [(255, 255, 255), (248, 135, 0), (255, 207, 0), (255, 255, 0),
                  (174, 0, 0), (208, 112, 0), (255, 0, 0)]

color_velocity_pairs_ceil = [
    ((0, 224, 255), -28), ((0, 128, 255), -27), ((50, 0, 150), -20),
    ((0, 251, 144), -15), ((0, 187, 144), -10), ((0, 143, 0), -5), ((205, 192, 159), -1),
    ((255, 255, 255), 1), ((248, 135, 0), 5), ((255, 207, 0), 10), ((255, 255, 0), 15),
    ((174, 0, 0), 20), ((208, 112, 0), 27), ((255, 0, 0), 28)
]

color_velocity_pairs = [
    ((0, 224, 255), -27.5), ((0, 128, 255), -23.5), ((50, 0, 150), -17.5),
    ((0, 251, 144), -12.5), ((0, 187, 144), -7.5), ((0, 143, 0), -3), ((205, 192, 159), -0.5),
    ((255, 255, 255), 0.5), ((248, 135, 0), 3), ((255, 207, 0), 7.5), ((255, 255, 0), 12.5),
    ((174, 0, 0), 17.5), ((208, 112, 0), 23.5), ((255, 0, 0), 27.5)
]

v_base_path = '../RadarPreprocess/sources/blank.png'

radar_area = (38, 730)
radar_center = (384, 384)
center_diameter = 9
surrounding_offsets = [(0, -1), (0, 1), (-1, 0), (1, 0)]
radar_diameter = 384 - 38
legend_area = (769, 935, 2, 570)    # (769, 2) (935, 570)
blur_threshold = 29.5
area_need_filled_threshold = 45
max_color_sale = [(0, 224, 255), (255, 0, 0)]
narrow_fill_threshold = 36
complex_fill_check_threshold = 9


def is_color_equal(color1, color2, delta):
    """Check if two colors are similar within a given delta."""
    return all(abs(c1 - c2) <= delta for c1, c2 in zip(color1[:3], color2[:3]))
