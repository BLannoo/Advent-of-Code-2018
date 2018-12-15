import copy

TRANSLATIONS_CART_SYMBOL_TO_UNDERLYING_TRACK = [(">", "-"), ("<", "-"), ("v", "|"), ("^", "|")]

CART_MOVEMENTS = [(">", 1, 0), ("<", -1, 0), ("v", 0, 1), ("^", 0, -1)]

CART_ROTATIONS = [
    ("v", "\\", ">"), ("v", "/", "<"), ("v", "|", "v"),
    ("^", "\\", "<"), ("^", "/", ">"), ("^", "|", "^"),
    (">", "\\", "v"), (">", "/", "^"), (">", "-", ">"),
    ("<", "\\", "^"), ("<", "/", "v"), ("<", "-", "<")
]

TURN_LEFT = [("v", ">"), (">", "^"), ("^", "<"), ("<", "v")]
TURN_RIGHT = [("v", "<"), ("<", "^"), ("^", ">"), (">", "v")]
GO_STRAIGHT = [("v", "v"), ("<", "<"), ("^", "^"), (">", ">")]


class Cart:
    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.direction = direction
        self.action_count = 0

    def choose_direction(self):
        action = [TURN_LEFT, GO_STRAIGHT, TURN_RIGHT][self.action_count % 3]
        self.action_count += 1
        return [
            turn[1]
            for turn in action
            if turn[0] == self.direction
        ][0]

    def __repr__(self):
        return (
                'Cart(' +
                'x=' + str(self.x) + ', '
                                     'y=' + str(self.y) + ', '
                                                          'direction=\'' + self.direction + '\')'
        )

    def __eq__(self, other):
        return (
                self.x == other.x
                and
                self.y == other.y
                and
                self.direction == other.direction
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
            # print('doing iteration: ', i)
            self.__update()
            if len(self.carts) == 1:
                print(
                    'stopped at iteration: ', i,
                    '\nwith cart:', self.carts
                )
                return

    def __update(self):
        # print('before:\n', self)
        for i in range(len(self.carts)):
            self.carts[i] = self.move_cart(self.carts[i])
            self.check_for_collision()
        self.remove_collided_carts()
        # print('after\n', self)

    def remove_collided_carts(self):
        for cart in [
            cart
            for cart in self.carts
            if cart.direction == 'X'
        ]:
            print('crashed cart:', cart)
        self.carts = [
            cart
            for cart in self.carts
            if not cart.direction == 'X'
        ]


    def move_cart(self, cart):
        if cart.direction == 'X':
            return cart
        for direction in CART_MOVEMENTS:
            if cart.direction == direction[0]:
                cart.x += direction[1]
                cart.y += direction[2]
        track_under_cart = self.track[cart.y][cart.x]
        if track_under_cart == '+':
            cart.direction = cart.choose_direction()
            return cart
        for rotation in CART_ROTATIONS:
            if cart.direction == rotation[0] and track_under_cart == rotation[1]:
                cart.direction = rotation[2]
                break
        return cart

    def check_for_collision(self):
        for i in range(len(self.carts)):
            for j in range(i + 1, len(self.carts)):
                if (
                        self.carts[i].x == self.carts[j].x
                        and
                        self.carts[i].y == self.carts[j].y
                ):
                    self.carts[i].direction = 'X'
                    self.carts[j].direction = 'X'

    def __repr__(self):
        track_with_carts = copy.deepcopy(self.track)
        for cart in self.carts:
            track_with_carts[cart.y][cart.x] = cart.direction
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


if __name__ == "__main__":
    track = create_track('../../data/day13.txt')
    track.update(100000)
