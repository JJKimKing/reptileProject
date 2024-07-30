from pyecharts import options as opts
from pyecharts.charts import Line
from pyecharts.globals import RenderType
from pyecharts.options import AnimationOpts, AriaOpts, AriaLabelOpts, AriaDecalOpts

# bar = {
#     Bar(init_opts=opts.InitOpts(theme=ThemeType.LIGHT))
#     .add_xaxis(["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"])
#     .add_yaxis("商家A", [5, 20, 36, 10, 75, 90])
#     .add_yaxis("商家B", [15, 6, 45, 20, 35, 66])
#     # .set_global_opts(title_opts=opts.TitleOpts(title='主标题',subtitle='副标题'))
#     .set_global_opts(title_opts={"title": "主标题", "subtitle": "副标题"})
#     .render("pyecharts_demo.html")
# }

line = {
    Line(
        init_opts=opts.InitOpts(
            animation_opts=AnimationOpts(
                animation_easing='elasticOut'
            ),
            aria_opts=AriaOpts(
                is_enable=True,
                # 无障碍标签配置项
                aria_label_opts=AriaLabelOpts(
                    is_enable=True,
                ),
                # 无障碍贴花配置项
                aria_decal_opts=AriaDecalOpts(
                    is_show=True,
                    decals_symbol='triangle',
                    decals_color='rgba(0, 0, 0, 0.2)'
                )
            ),
            renderer=RenderType.SVG,
        ),
        render_opts=opts.RenderOpts(
            # 是否在渲染 HTML 时嵌入 JS 文件
            is_embed_js=False
        )
    )
    .add_xaxis(["美国", '英国', '法国'])
    .add_yaxis("GDP", ['30', '20', '10'])
    .set_global_opts(title_opts={"title": "主标题", "subtitle": "副标题"})
    .render()
}
