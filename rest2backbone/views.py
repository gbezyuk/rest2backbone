from django.views.generic import TemplateView
from api import ModelMaker
from django.utils.safestring import SafeString


class restApi(TemplateView):
    template_name = 'rest2backbone/api.js'
    
    def render_to_response(self, context, **response_kwargs):
        if context.get('params'):  # for django 1.4 compatibility
            context = context['params']
        if not context.get('router'):
            raise ValueError('router param missing')
        maker = ModelMaker(context['router'], context.get('url_prefix'))
        context['models'] = SafeString(maker.toJS())
        return TemplateView.render_to_response(self, context, mimetype='text/javascript')