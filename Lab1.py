import math

class Object:

    def __init__(self, name, size_x, size_y, size_z, coordinate_x, coordinate_y, coordinate_z) -> None:
        self.name = name
        self.size_x = size_x
        self.size_y = size_y
        self.size_z = size_z
        self.coordinate_x = coordinate_x
        self.coordinate_y = coordinate_y
        self.coordinate_z = coordinate_z

        pass

    def intersection(self, another_thing):
        delta_X = math.fabs(self.coordinate_x - another_thing.coordinate_x)
        delta_Y = math.fabs(self.coordinate_y - another_thing.coordinate_y)
        delta_Z = math.fabs(self.coordinate_z - another_thing.coordinate_z)

        intersection_X = delta_X <= ((self.size_x / 2) + (another_thing.size_x / 2))
        intersection_Y = delta_Y <= ((self.size_y / 2) + (another_thing.size_y / 2))
        intersection_Z = delta_Z <= ((self.size_z / 2) + (another_thing.size_z / 2))

        if intersection_X:
            if intersection_Y:
                if intersection_Z:

                    return True

        return False

class Furniture(Object):

    def __init__(self, name, size_x, size_y, size_z, coordinate_x, coordinate_y, coordinate_z, material) -> None:
        super().__init__(name, size_x, size_y, size_z, coordinate_x, coordinate_y, coordinate_z)
        self.material = material

        pass

class Devices(Object):

    def __init__(self, name, size_x, size_y, size_z, coordinate_x, coordinate_y, coordinate_z, model) -> None:
        super().__init__(name, size_x, size_y, size_z, coordinate_x, coordinate_y, coordinate_z)
        self.model = model

        pass

    def switch_ON():
        print('The device is switched on')

    def switch_OFF():
        print('The device is switched off')

class KitchenProject:

    def __init__(self, size_x, size_y, size_z, objects) -> None:
        self.size_x = size_x
        self.size_y = size_y
        self.size_z = size_z
        self.objects = objects

        pass

    def acceptance_test(self):
        for object1 in self.objects:
            for object2 in self.objects:
                if object1 != object2:
                    
                    # Пересечение
                    if object1.intersection(object2):

                        return False
                    
                    if object1.material != object2.material: 
                        # Расстояние
                        delta_X = object1.coordinate_x - object2.coordinate_x
                        delta_Y = object1.coordinate_y - object2.coordinate_y
                        delta_Z = object1.coordinate_z - object2.coordinate_z
                        distance = math.sqrt((delta_X ** 2) + (delta_Y ** 2) + (delta_Z ** 2))
                        if distance < 2:

                            return False
                        
                # Объем объекта и кухни
                object1_S = object1.size_x * object1.size_y * object1.size_z
                object2_S = object2.size_x * object2.size_y * object2.size_z
                kitchen_S = self.size_x * self.size_y * self.size_z
                if object1_S > kitchen_S or object2_S > kitchen_S:

                    return False


        # Высота техники                
        for device in self.objects:
            if device.coordinate_z > 0:
                    
                    return False
            
        return True

# Входные данные
cabinet = Furniture("Кухонный шкаф", 10, 20, 2, 8, 10, 0, "Дерево")
chair = Furniture("Стул", 1, 2, 1, 2, 3, 0, "Дерево")
# table = Furniture("Стол", 10, 20, 2, 1, 2, 0, "Дерево")
# fridge = Devices("Холодильник", 5, 5, 3, 1, 2, 2, "Samsung")

project = KitchenProject(100, 50, 3, [cabinet, chair])

if project.acceptance_test():
    print("Условие задачи выполнено")
else:
    print("Условие задачи не выполнено")


'''
Добавлю от себя. Для удобства можно переделать передачу размеров и координат через множества/списки, 
но в данном случае было решено сделать отдельные перемены под каждый размер и координату, 
чтобы было удобнее разрабатывать и проверять результаты на корректность
'''

