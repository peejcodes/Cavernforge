from plants import Plants


plants_dictionary = {
    'rose': {
        'name': 'Rose',
        'sprite': 'path/to/rose_sprite.png',
        'weight': 5,
        'grow_time': 30,
        'water_needs': 'moderate',
        'sunlight_needs': 'full sun',
        'soil_needs': 'well-drained',
        'temperature_needs': (55, 75),
        'total_growth_stages': 4,
        'harvest_range': (0, 0)
    },
    'sunflower': {
        'name': 'Sunflower',
        'sprite': 'path/to/sunflower_sprite.png',
        'weight': 3,
        'grow_time': 20,
        'water_needs': 'moderate',
        'sunlight_needs': 'full sun',
        'soil_needs': 'well-drained',
        'temperature_needs': (65, 85),
        'total_growth_stages': 3,
        'harvest_range': (0, 0)
    },
    'tulip': {
        'name': 'Tulip',
        'sprite': 'path/to/tulip_sprite.png',
        'weight': 2,
        'grow_time': 15,
        'water_needs': 'low',
        'sunlight_needs': 'partial shade',
        'soil_needs': 'well-drained',
        'temperature_needs': (55, 75),
        'total_growth_stages': 3,
        'harvest_range': (0, 0)
    },
    'lavender': {
        'name': 'Lavender',
        'sprite': 'path/to/lavender_sprite.png',
        'weight': 2,
        'grow_time': 25,
        'water_needs': 'low',
        'sunlight_needs': 'full sun',
        'soil_needs': 'well-drained',
        'temperature_needs': (60, 80),
        'total_growth_stages': 4,
        'harvest_range': (0, 0)
    },
    'carnation': {
        'name': 'Carnation',
        'sprite': 'path/to/carnation_sprite.png',
        'weight': 4,
        'grow_time': 25,
        'water_needs': 'moderate',
        'sunlight_needs': 'partial shade',
        'soil_needs': 'well-drained',
        'temperature_needs': (60, 75),
        'total_growth_stages': 4,
        'harvest_range': (0, 0)
    },
    'daisy': {
        'name': 'Daisy',
        'sprite': 'path/to/daisy_sprite.png',
        'weight': 2,
        'grow_time': 15,
        'water_needs': 'low',
        'sunlight_needs': 'partial shade',
        'soil_needs': 'well-drained',
        'temperature_needs': (55, 75),
        'total_growth_stages': 3,
        'harvest_range': (0, 0)
    },
    'orchid': {
        'name': 'Orchid',
        'sprite': 'path/to/orchid_sprite.png',
        'weight': 2,
        'grow_time': 35,
        'water_needs': 'moderate',
        'sunlight_needs': 'partial shade',
        'soil_needs': 'well-drained',
        'temperature_needs': (65, 80),
        'total_growth_stages': 5,
        'harvest_range': (0, 0)
    },
    'lily': {
        'name': 'Lily',
        'sprite': 'path/to/lily_sprite.png',
        'weight': 3,
        'grow_time': 20,
        'water_needs': 'moderate',
        'sunlight_needs': 'partial shade',
        'soil_needs': 'well-drained',
        'temperature_needs': (60, 75),
        'total_growth_stages': 4,
        'harvest_range': (0, 0)
    },
    'cactus': {
        'name': 'Cactus',
        'sprite': 'path/to/cactus_sprite.png',
        'weight': 4,
        'grow_time': 40,
        'water_needs': 'low',
        'sunlight_needs': 'full sun',
        'soil_needs': 'sandy',
        'temperature_needs': (70, 90),
        'total_growth_stages': 5,
        'harvest_range': (0, 0)
    },
    'daffodil': {
        'name': 'Daffodil',
        'sprite': 'path/to/daffodil_sprite.png',
        'weight': 2,
        'grow_time': 15,
        'water_needs': 'low',
        'sunlight_needs': 'full sun',
        'soil_needs': 'well-drained',
        'temperature_needs': (55, 70),
        'total_growth_stages': 3,
        'harvest_range': (0, 0)
    },
    'hydrangea': {
        'name': 'Hydrangea',
        'sprite': 'path/to/hydrangea_sprite.png',
        'weight': 4,
        'grow_time': 30,
        'water_needs': 'high',
        'sunlight_needs': 'partial shade',
        'soil_needs': 'moist',
        'temperature_needs': (65, 80),
        'total_growth_stages': 4,
        'harvest_range': (0, 0)
    },
    'geranium': {
        'name': 'Geranium',
        'sprite': 'path/to/geranium_sprite.png',
        'weight': 3,
        'grow_time': 25,
        'water_needs': 'moderate',
        'sunlight_needs': 'full sun',
        'soil_needs': 'well-drained',
        'temperature_needs': (65, 85),
        'total_growth_stages': 4,
        'harvest_range': (0, 0)
    },
    'pansy': {
        'name': 'Pansy',
        'sprite': 'path/to/pansy_sprite.png',
        'weight': 2,
        'grow_time': 15,
        'water_needs': 'moderate',
        'sunlight_needs': 'partial shade',
        'soil_needs': 'well-drained',
        'temperature_needs': (55, 70),
        'total_growth_stages': 3,
        'harvest_range': (0, 0)
    },
    'iris': {
        'name': 'Iris',
        'sprite': 'path/to/iris_sprite.png',
        'weight': 3,
        'grow_time': 20,
        'water_needs': 'moderate',
        'sunlight_needs': 'partial shade',
        'soil_needs': 'well-drained',
        'temperature_needs': (60, 75),
        'total_growth_stages': 4,
        'harvest_range': (0, 0)
    },
    'chrysanthemum': {
        'name': 'Chrysanthemum',
        'sprite': 'path/to/chrysanthemum_sprite.png',
        'weight': 4,
        'grow_time': 25,
        'water_needs': 'moderate',
        'sunlight_needs': 'full sun',
        'soil_needs': 'well-drained',
        'temperature_needs': (60, 75),
        'total_growth_stages': 4,
        'harvest_range': (0, 0)
    },
    'carnation': {
        'name': 'Carnation',
        'sprite': 'path/to/carnation_sprite.png',
        'weight': 4,
        'grow_time': 25,
        'water_needs': 'moderate',
        'sunlight_needs': 'partial shade',
        'soil_needs': 'well-drained',
        'temperature_needs': (60, 75),
        'total_growth_stages': 4,
        'harvest_range': (0, 0)
    },
    'dandelion': {
        'name': 'Dandelion',
        'sprite': 'path/to/dandelion_sprite.png',
        'weight': 2,
        'grow_time': 10,
        'water_needs': 'low',
        'sunlight_needs': 'full sun',
        'soil_needs': 'well-drained',
        'temperature_needs': (50, 75),
        'total_growth_stages': 3,
        'harvest_range': (0, 0)
    },
    'marigold': {
        'name': 'Marigold',
        'sprite': 'path/to/marigold_sprite.png',
        'weight': 2,
        'grow_time': 15,
        'water_needs': 'low',
        'sunlight_needs': 'full sun',
        'soil_needs': 'well-drained',
        'temperature_needs': (60, 80),
        'total_growth_stages': 3,
        'harvest_range': (0, 0)
    },
    'snapdragon': {
        'name': 'Snapdragon',
        'sprite': 'path/to/snapdragon_sprite.png',
        'weight': 3,
        'grow_time': 20,
        'water_needs': 'moderate',
        'sunlight_needs': 'partial shade',
        'soil_needs': 'well-drained',
        'temperature_needs': (60, 75),
        'total_growth_stages': 4,
        'harvest_range': (0, 0)
    },
    'zinnia': {
        'name': 'Zinnia',
        'sprite': 'path/to/zinnia_sprite.png',
        'weight': 3,
        'grow_time': 20,
        'water_needs': 'moderate',
        'sunlight_needs': 'full sun',
        'soil_needs': 'well-drained',
        'temperature_needs': (70, 85),
        'total_growth_stages': 4,
        'harvest_range': (0, 0)
    },
    'hibiscus': {
        'name': 'Hibiscus',
        'sprite': 'path/to/hibiscus_sprite.png',
        'weight': 4,
        'grow_time': 30,
        'water_needs': 'moderate',
        'sunlight_needs': 'full sun',
        'soil_needs': 'well-drained',
        'temperature_needs': (65, 80),
        'total_growth_stages': 4,
        'harvest_range': (0, 0)
    },
    'poinsettia': {
        'name': 'Poinsettia',
        'sprite': 'path/to/poinsettia_sprite.png',
        'weight': 5,
        'grow_time': 35,
        'water_needs': 'moderate',
        'sunlight_needs': 'partial shade',
        'soil_needs': 'well-drained',
        'temperature_needs': (60, 70),
        'total_growth_stages': 5,
        'harvest_range': (0, 0)
    }
}

class Flowers:
    def __init__(self, name):
        super().__init__(name)

        
        
poinsettia = Flowers('poinsettia')