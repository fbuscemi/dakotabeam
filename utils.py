import matplotlib.pyplot as plt


def plot_section(beam, results={}):
    vertices = [(0, 0), 
                (beam.blf/2, 0),
                (beam.blf/2, beam.tlf),
                (beam.tw/2, beam.tlf),
                (beam.tw/2, beam.h - beam.tuf),
                (beam.buf/2, beam.h - beam.tuf),
                (beam.buf/2, beam.h),
                (-beam.buf/2, beam.h),
                (-beam.buf/2, beam.h - beam.tuf),
                (-beam.tw/2, beam.h - beam.tuf),
                (-beam.tw/2, beam.tlf),
                (-beam.blf/2, beam.tlf),
                (-beam.blf/2, 0),
               ]
    codes = [mpl.path.Path.MOVETO] + [mpl.path.Path.LINETO]*12
    p = mpl.path.Path(vertices, codes)

    fig, ax = plt.subplots()
    ax.add_patch(mpl.patches.PathPatch(p))
    bbox = p.get_extents()
    ax.set_xlim(bbox.intervalx)
    ax.set_ylim(bbox.intervaly)
    ax.set_aspect(1.0)
    ax.set_axis_off()

    description = f"h = {beam.h:.1f}\n" +\
    f"tw = {beam.tw:.2f}\n" +\
    f"buf = {beam.buf:.1f}\n" +\
    f"tuf = {beam.tuf:.2f}\n" +\
    f"blf = {beam.blf:.1f}\n" +\
    f"tlf = {beam.tlf:.2f}\n\n" +\
    f"material = {beam.matname}\n\n" +\
    f"mass = {beam.mass():.2f}\n" +\
    f"cost = {beam.cost():.1f}"
    
    #f"area = {beam.area:.1f}\n" +\

    ax.text(beam.buf/2 + 20, beam.h, description,  
            horizontalalignment='left',
            verticalalignment='top',
    );

    rows = ['wmax', 'rf_t_uf', 'rf_t_lf', 'rf_c_uf', 'rf_c_lf', 'rf_lb_uf',
              'rf_lb_lf', 'rf_s_web', 'rf_wb', 'rf_lat']
    if results:
        res_text = "\n".join(["%s = %.2f" % (k, results[k]) for k in rows])
        ax.text(beam.buf/2 + 100, beam.h, res_text,  
                horizontalalignment='left',
                verticalalignment='top',
        );
        