world = [[], [], []]  
collision_pairs = {}

def add_oject(o, depth=1):
    world[depth].append(o)

def add_objects(ol, depth=1):
    world[depth] += ol

def remove_object(o):
    for layer in world:
        if o in layer:
            layer.remove(o)
            break
    remove_collision_object(o)

def add_collision_pair(group, a, b):
    if group not in collision_pairs:
        collision_pairs[group] = [[], []]

    objects_a, objects_b = collision_pairs[group]
    if a is not None and a not in objects_a:
        objects_a.append(a)
    if b is not None and b not in objects_b:
        objects_b.append(b)

def remove_collision_object(o):
    for objects_a, objects_b in collision_pairs.values():
        while o in objects_a:
            objects_a.remove(o)
        while o in objects_b:
            objects_b.remove(o)

def collide(a, b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()
    return not (right_a < left_b or left_a > right_b or
                top_a < bottom_b or bottom_a > top_b)

def handle_collisions():
    for group, (objects_a, objects_b) in collision_pairs.items():
        for a in objects_a[:]:
            for b in objects_b[:]:
                if a not in objects_a or b not in objects_b:
                    continue
                if collide(a, b):
                    handler_a = getattr(a, 'handle_collision', None)
                    if handler_a is not None:
                        handler_a(b, group)
                    handler_b = getattr(b, 'handle_collision', None)
                    if handler_b is not None:
                        handler_b(a, group)

def update():
    for layer in world:
        for o in layer[:]:
            o.update()
    handle_collisions()

def render():
    for layer in world:
        for o in layer[:]:
            o.draw()




def clear():
    for layer in world:
        layer.clear()
    collision_pairs.clear()
