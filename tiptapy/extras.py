from . import BaseNode, register_renderer


class FeaturedImage(BaseNode):
    type = "featuredimage"

    def inner_render(self, node) -> str:
        special_attrs_map = {'caption': 'figcaption'}
        attrs = node.get("attrs", {})
        html = ""
        attrs_s = " ".join(f'{k}="{v}"'
                           for k, v in attrs.items()
                           if k not in special_attrs_map and v.strip()
                           )
        if attrs_s:
            inner_html = f"<img {attrs_s}>"
            if attrs.get('caption', '').strip():
                tag = special_attrs_map['caption']
                inner_html += f"<{tag}>{attrs['caption']}</{tag}>"
            html = f'<figure class="featured-image">{inner_html}</figure>'
        return html


register_renderer(FeaturedImage)
