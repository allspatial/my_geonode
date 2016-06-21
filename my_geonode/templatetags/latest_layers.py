from django import template
from geonode.layers.models import Layer
from geonode import settings
from guardian.shortcuts import get_objects_for_user

register = template.Library()


@register.assignment_tag(takes_context=True)
def last_three_layers(context):

    request = context['request']

    layers = Layer.objects.order_by('-upload_session__date')

    if settings.RESOURCE_PUBLISHING:
        layers = layers.filter(is_published=True)

    if not settings.SKIP_PERMS_FILTER:
        authorized = get_objects_for_user(
            request.user, 'base.view_resourcebase').values('id')

    if not settings.SKIP_PERMS_FILTER:
        layers = layers.filter(id__in=authorized)

    layers = layers[:5]

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
