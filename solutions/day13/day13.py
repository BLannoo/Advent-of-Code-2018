import copy

TRANSLATIONS_CART_SYMBOL_TO_UNDERLYING_TRACK = [(">", "-"), ("<", "-"), ("V", "|"), ("^", "|")]

CART_MOVEMENTS = [(">", 1, 0), ("<", -1, 0), ("V", 0, 1), ("^", 0, -1)]

CART_ROTATIONS = [
    ("V", "\\", ">"), ("V", "/", "<"), ("V", "|", "V"),
    ("^", "\\", "<"), ("^", "/", ">"), ("^", "|", "^"),
    (">", "\\", "V"), (">", "/", "^"), (">", "-", ">"),
    ("<", "\\", "^"), ("<", "/", "V"), ("<", "-", "<")
]


class Cart:
    def __init__(self, x, y, dir):
        self.x = x
        self.y = y
        self.dir = dir

    def __repr__(self):
        return (
            'Cart(' +
            'x=' + str(self.x) + '; '
            'y=' + str(self.y) + '; '
            'dir=' + str(self.dir) + ')'
        )

    def __eq__(self, other):
        return (
            self.x == other.x
            and
            self.y == other.y
            and
            self.dir == other.dir
        )


class Track:
    def __init__(self, string_track_with_carts):
        lines = string_track_with_carts.strip("\n").split("\n")
        self.track = [list(line) for line in lines]
        self.carts = []
        for x in range(len(self.track)):
            for y in range(len(self.track[x])):
                for cart in TRANSLATIONS_CART_SYMBOL_TO_UNDERLYING_TRACK:
                    if self.track[x][y] == cart[0]:
                        self.carts.append(Cart(y, x, cart[0]))
                        self.track[x][y] = cart[1]

    def update(self, times):
        for i in range(times):
            print('doing iteration: ', i)
            self.__update()

    def check_for_collision(self):
        for i in range(len(self.carts)):
            for j in range(i+1, len(self.carts)):
                print('checking carts: i=', self.carts[i], '; j=', self.carts[j])
                if (
                        self.carts[i].x == self.carts[j].x
                        and
                        self.carts[i].y == self.carts[j].y
                ):
                    self.carts[i].dir = 'X'
                    self.carts[j].dir = 'X'
                    return self.carts[i], self.carts[j]
        return None, None

    def __update(self):
        print('before:\n', self)
        for i in range(len(self.carts)):
            self.carts[i] = self.move_cart(self.carts[i])
            self.check_for_collision()
        print('after\n', self)

    def move_cart(self, cart):
        for direction in CART_MOVEMENTS:
            if cart.dir == direction[0]:
                new_x = cart.x + direction[1]
                new_y = cart.y + direction[2]
        for rotation in CART_ROTATIONS:
            if cart.dir == rotation[0] and self.track[new_y][new_x] == rotation[1]:
                new_dir = rotation[2]
        return Cart(new_x, new_y, new_dir)

    def __repr__(self):
        track_with_carts = copy.deepcopy(self.track)
        for cart in self.carts:
            track_with_carts[cart.y][cart.x] = cart.dir
        return (
            "Carts:" + str(self.carts) + "\n" +
            "\n".join(["".join(track_with_carts[x]) for x in range(len(track_with_carts))]) +
            "\n"
        )

    def __eq__(self, other):
        return (
            self.track == other.track
            and
            self.carts == other.carts
        )


def create_track(file_name):
    with open(file_name, 'r') as track_string:
        return Track(''.join(track_string.readlines()))
