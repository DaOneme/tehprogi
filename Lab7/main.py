import math

class Polygon:
    def __init__(self, vertices):
        self.vertices = vertices

    @staticmethod
    def segment_dist(px, py, x1, y1, x2, y2):
        line_mag = math.hypot(x2 - x1, y2 - y1)
        if line_mag < 1e-15:
            return math.hypot(px - x1, py - y1)
        u = ((px - x1) * (x2 - x1) + (py - y1)*(y2 - y1)) / (line_mag**2)
        if u < 0:
            return math.hypot(px - x1, py - y1)
        elif u > 1:
            return math.hypot(px - x2, py - y2)
        else:
            ix = x1 + u*(x2 - x1)
            iy = y1 + u*(y2 - y1)
            return math.hypot(px - ix, py - iy)

    def point_pos(self, point):
        x0, y0 = point
        total_angle = 0.0
        n = len(self.vertices)
        eps = 1e-9

        for i in range(n):
            x1, y1 = self.vertices[i]
            x2, y2 = self.vertices[(i+1) % n]
            v1 = (x1 - x0, y1 - y0)
            v2 = (x2 - x0, y2 - y0)
            angle1 = math.atan2(v1[1], v1[0])
            angle2 = math.atan2(v2[1], v2[0])
            angle3 = angle2 - angle1

            dist = self.segment_dist(x0, y0, x1, y1, x2, y2)
            if dist < eps:
                return "0"

            if angle3 <= -math.pi:
                angle3 += 2 * math.pi
            elif angle3 > math.pi:
                angle3 -= 2 * math.pi
            total_angle += angle3

        total_deg = math.degrees(total_angle)
        if abs(total_deg - 360) < 1e-3 or abs(total_deg + 360) < 1e-3:
            return "1"
        else:
            return "-1"



def main():
    input_data = input("Введите вершины многоугольника (через пробел, например: x1 y1 x2 y2 ...), или путь к .txt файлу:\n").strip()

    if input_data.endswith('.txt'):
        try:
            with open(input_data, 'r') as f:
                lines = f.read().splitlines()
            vertices_str = lines[0]
            point_str = lines[1]
        except:
            print("Файл с таким именем не найден")
            return 0 
    else:
        vertices_str = input_data
        print("Введите точку для проверки (x y):")
        point_str = input().strip()
        
        
    vertices_list = list(map(float, vertices_str.split()))
    if len(vertices_list) % 2 != 0:
        print("Ошибка: количество чисел для вершин должно быть чётным.")
        return 0
    
    # Обработка входных данных
    vertices_list = list(map(float, vertices_str.split()))
    vertices = [(vertices_list[i], vertices_list[i+1]) for i in range(0, len(vertices_list), 2)]
    x0, y0 = map(float, point_str.split())

    poly = Polygon(vertices)
    result = poly.point_pos((x0, y0))
    print(f"Результат: {result}")

if __name__ == "__main__":
    main()