'''
交叉路口的红绿灯安排
描述：
E，C是单行道，A，B，D是双行道
分析：
路口共有13个可行方向：AB，AC，AD，BA，BC，BD，DA，DB，DC，EA，EB，EC，ED
需要从中确定一些可以同时开绿灯的方向组，也就是说，需要为所有可能方向做出一种安全分组，
保证位于每组里的行驶方向互不冲突，可以同时放行。
如果把所有行驶方向画在一张纸上，就做出了一个冲突图。
这样的图构成了“图”的数据结构。元素称为顶点，连线称为边或弧，相互之间有边的顶点称为邻接顶点。
有了冲突图，寻找安全分组问题就可以说成：为冲突图中的顶点确定一种分组，保证属于同一组的所有顶点互不邻接。
贪心算法：

'''
def coloring(G):    # 做图G的着色
    color = 0
    groups = set()
    verts = vertices(G) # 取得G的所有顶点，依赖于图的表示
    while verts:    # 如果集合不空
        new_group = set()
        for v in list(verts):
            if not_adjacent_with_set(v, newgroup, G):
                new_group.add(v)
                verts.remove(v)
        groups.add((color, new_group))
        color += 1 
    return groups