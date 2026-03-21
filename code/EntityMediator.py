from code.Const import WIN_WIDTH
from code.EnemyShot import EnemyShot
from code.PlayerShot import PlayerShot
from code.enemy import Enemy
from code.entity import Entity


class EntityMediator:

    @staticmethod
    def __verify_collision_window(ent: Entity):
        if isinstance(ent, Enemy):
            if ent.rect.right < 0:
                ent.health = 0
        if 'Shot' in ent.name:  # Se for qualquer tipo de tiro
            if ent.rect.left >= WIN_WIDTH or ent.rect.right <= 0:
                ent.health = 0

        if isinstance(ent,PlayerShot):
            if ent.rect.left >= WIN_WIDTH:
                ent.health = 0
        if isinstance(ent, EnemyShot):
            if ent.rect.left <= 0:
                ent.health = 0

    @staticmethod
    def verify_collision(entity_list: list[Entity]):
        for i in range(len(entity_list)):
            test_entity = entity_list[i]
            EntityMediator.__verify_collision_window(test_entity)

    # @staticmethod
    # def verify_health(entity_list: list[Entity]):
    #     for ent in entity_list:
    #         if ent.health <= 0:
    #             entity_list.remove(ent)
    @staticmethod
    def verify_health(entity_list: list[Entity]):
        # Cria uma cópia da lista ou usa list comprehension para filtrar os vivos
        for ent in entity_list[:]:  # O [:] cria uma cópia para a iteração ser segura
            if ent.health <= 0:
                entity_list.remove(ent)