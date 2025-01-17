import math
from db_utils import session, SinusoidalData

def generate_sinusoidal_data():
    """Generate sinusoidal data and store it in the database."""
    data = [
        SinusoidalData(x=x, y=math.sin(x))
        for x in [i * 0.1 for i in range(0, 10000)]
    ]
    session.add_all(data)
    session.commit()
    print("Sinusoidal data generated and stored in the database.")

if __name__ == "__main__":
    generate_sinusoidal_data()