def _get_or_create_obj_by_id(klass, id, **kwargs):
    if not id:
        return None
    if len(klass.objects.filter(id=id)) == 0:
        kwargs["id"] = id
        obj = klass.objects.create(**kwargs)
        return obj
    return klass.objects.filter(id=id).first()


def _get_or_create_obj(klass, name, **kwargs):
    if not name:
        return None
    if len(klass.objects.filter(name=name)) == 0:
        kwargs["name"] = name
        obj = klass.objects.create(**kwargs)
        return obj
    return klass.objects.filter(name=name).first()

