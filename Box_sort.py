'''
Write a Box class whose init method takes three parameters and uses them to initialize the private length, width and height data members of a Box. It should also have a method named volume that returns the volume of the Box. It should have get methods named get_length, get_width, and get_height.

Write a separate function named box_sort (not part of the Box class) that uses insertion sort to sort a list of Boxes from greatest volume to least volume.
'''

class Box():
    def __init__(self, length, width, height):
        self._length = length
        self._width = width
        self._height = height

        def get_length(self):
            return self._length
        def get_width(self):
            return self._width
        def get_height(self):
            return self._height
        def get_volume(self):
            return self._length*self._width*self._height



def box_sort(box_list):
  """
  Sorts a_list in ascending order
  """
    box_volumes = []
    for b in box_list:
        box_volumes.append(b.get_volume())

    for index in range(1, len(box_volumes)):
        value = box_volumes[index]
        pos = index - 1
        while pos >= 0 and box_volumes[pos] > value:
            box_volumes[pos + 1] = box_volumes[pos]
            pos -= 1
        box_volumes[pos + 1] = value

    return box_volumes




b1 = Box(3.4, 19.8, 2.1)
b2 = Box(1.0, 1.0, 1.0)
b3 = Box(8.2, 8.2, 4.5)
box_list = [b1, b2, b3]
box_sort(box_list)
