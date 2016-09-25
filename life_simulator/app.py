import pygame

from person.person import Person
from activity.activity import Attributes, activities


class AttributeRect(pygame.Rect):
    def __init__(self, rect, label):
        super().__init__(rect)
        self.rect = rect
        self.label = label


class DrawGame(object):
    FLAX = (238, 205, 134)
    VIOLET = (61, 50, 66)
    LOTUS = (122, 62, 72)
    ORANGE = (225, 137, 66)
    RED = (185, 88, 53)

    def __init__(self):
        pygame.init()
        self.width = 700
        self.height = 500

        self.size = (self.width, self.height)
        self.screen = pygame.display.set_mode(self.size)
        self.clock = pygame.time.Clock()

    def __exit__(self):
        pygame.quit()

    def draw_game(self, player):
        self.screen.fill(self.FLAX)
        self.draw_stats(0, player)
        self.draw_player(200, player)
        attr_rects = self.draw_activities(400, player)
        pygame.display.flip()
        return attr_rects

    def draw_stats(self, start_width,  player):
        monospace_font = pygame.font.SysFont("monospace", 14)
        width_of_stat = self.width // 5
        height_of_stat = self.height // (len(player.stats) + 1)
        curr_height = height_of_stat // 2
        for attr, value in player.stats.items():
            pygame.draw.rect(self.screen, self.ORANGE, (start_width, curr_height, width_of_stat, height_of_stat - 0.1), 0)
            label = monospace_font.render(attr + " " + str(value), 0, self.VIOLET)
            self.screen.blit(label, (start_width, curr_height))
            curr_height += height_of_stat

    def draw_player(self, start_width, player):
        monospace_font = pygame.font.SysFont("monospace", 14)
        label = monospace_font.render(str(player.time.current_date), 0, self.VIOLET)
        self.screen.blit(label, (start_width, 200))

    def draw_activities(self, start_width, player):
        monospace_font = pygame.font.SysFont("monospace", 14)
        width_of_stat = self.width // 5
        height_of_stat = self.height // (len(activities().items()) + 1)
        curr_height = height_of_stat // 2

        attr_rects = []
        for attr, value in activities().items():
            rect_attr = (start_width, curr_height, width_of_stat, height_of_stat - 0.1)
            rect = pygame.draw.rect(self.screen, self.ORANGE, rect_attr, 0)
            attr_rects.append(AttributeRect(rect, attr))
            label = monospace_font.render(attr + " " + str(value.duration), 0, self.VIOLET)
            self.screen.blit(label, (start_width, curr_height))
            curr_height += height_of_stat
        return attr_rects


def main():
    game = DrawGame()
    done = False
    attr_rects = []
    player = Person(Attributes)
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                clicked_attrs = [s for s in attr_rects if s.collidepoint(pos)]
                for cc in clicked_attrs:
                    player.apply_activity(activities()[cc.label]())
        attr_rects = game.draw_game(player)
        game.clock.tick(60)

if __name__ == "__main__":
    main()
