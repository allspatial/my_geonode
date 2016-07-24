from django import template
from geonode.layers.models import Layer
from geonode.maps.models import Map
from geonode import settings
from guardian.shortcuts import get_objects_for_user

register = template.Library()


@register.assignment_tag(takes_context=True)
def lastest_layers(context):

    request = context['request']

    layers = Layer.objects.order_by('-upload_session__date')

    if settings.RESOURCE_PUBLISHING:
        layers = layers.filter(is_published=True)

    if not settings.SKIP_PERMS_FILTER:
        authorized = get_objects_for_user(
            request.user, 'base.view_resourcebase').values('id')

    if not settings.SKIP_PERMS_FILTER:
        layers = layers.filter(id__in=authorized)

    layers = layers[:3]

    layer_list = list()

    for layer in layers:
        featured_layer = dict()
        featured_layer['title'] = layer.title
        upload_timestamp = layer.upload_session.date
        featured_layer['date'] = upload_timestamp.date()
        featured_layer['owner'] = layer.owner
        featured_layer['thumbnail_url'] = layer.thumbnail_url
        featured_layer['detail_url'] = layer.detail_url
        featured_layer['abstract'] = layer.abstract
        layer_list.append(featured_layer)

    return layer_list


@register.assignment_tag(takes_context=True)
def featured_maps(context):

    request = context['request']

    maps = Map.objects.order_by('-popular_count')

    if settings.RESOURCE_PUBLISHING:
        maps = maps.filter(is_published=True)

    if not settings.SKIP_PERMS_FILTER:
        authorized = get_objects_for_user(
            request.user, 'base.view_resourcebase').values('id')

    if not settings.SKIP_PERMS_FILTER:
        maps = maps.filter(id__in=authorized)

    maps = maps[:3]

    map_list = list()

    for map in maps:
        featured_map = dict()
        featured_map['title'] = map.title
        modified_timestamp = map.last_modified
        featured_map['date'] = modified_timestamp.date()
        featured_map['owner'] = map.owner
        featured_map['thumbnail_url'] = map.thumbnail_url
        featured_map['view_url'] = map.detail_url + "/view"
        featured_map['abstract'] = map.abstract
        featured_map['popular_count'] = map.popular_count
        map_list.append(featured_map)

    return map_list