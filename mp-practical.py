import random as rand
import matplotlib.pyplot as plt


class RandomPoint():

    def __init__(self, sizex=100, sizey=100, num_points=500):
        self.num_points = num_points
        self.x_val = []
        self.y_val = []
        self.p0 = {
            "x": 50,
            "y": 50
        }
        self.traingl = [
            {
                "x": 0,
                "y": 0
            },
            {
                "x": sizex,
                "y": 0
            },
            {
                "x": sizex // 2,
                "y": sizey
            }
        ]

    def random_vertex(self):
        temp = rand.randint(0, 2)
        return self.traingl[temp]

    def middle(self, start, end):
        x = (start["x"] + end["x"]) // 2
        y = (start["y"] + end["y"]) // 2
        return {"x": x, "y": y}

    def finding(self):
        for index in range(self.num_points):
            vertex = self.random_vertex()
            p1 = self.middle(self.p0, vertex)
            self.x_val.append(p1["x"])
            self.y_val.append(p1["y"])
            self.p0["x"] = p1.get("x")
            self.p0["y"] = p1.get("y")


rs = RandomPoint(1000, 1000, 25000)

rs.finding()
plt.figure(figsize=(15, 10))
point_numbers = list(range(rs.num_points))
plt.scatter(rs.x_val, rs.y_val, s=0.1)
plt.show()