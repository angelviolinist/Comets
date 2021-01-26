import pandas as pd
import matplotlib.pyplot as plt

# 289P
# 2035-Jan-01 00:00:00.0000,  2.523036803836940E-02,  4.368502806239363E+00,
# 2035-Jan-31 08:00:00.0000,  2.433720079476427E-02,  4.213855691928690E+00,
# 2035-Mar-02 16:00:00.0000,  2.244564857083295E-02,  3.886343576931959E+00,
# 2035-Apr-02 00:00:00.0000,  1.973840143984310E-02,  3.417598266878330E+00,
# 2035-May-02 08:00:00.0000,  1.647705205150560E-02,  2.852913125012276E+00,
# 2035-Jun-01 16:00:00.0000,  1.295818931399763E-02,  2.243640928895386E+00,
# 2035-Jul-02 00:00:00.0000,  9.480431229751441E-03,  1.641485782868710E+00,
# 2035-Aug-01 08:00:00.0000,  6.321255940494604E-03,  1.094491537856798E+00,
# 2035-Aug-31 16:00:00.0000,  3.710707220478834E-03,  6.424890386514592E-01,
# 2035-Oct-01 00:00:00.0000,  1.774643787670178E-03,  3.072700467437756E-01,
# 2035-Oct-31 08:00:00.0000,  5.434166251286647E-04,  9.408967194697801E-02,
# 2035-Nov-30 16:00:00.0000,  1.071641839857240E-03,  1.855490327204289E-01,
# 2035-Dec-31 00:00:00.0000,  1.991500979476300E-03,  3.448177055618138E-01,

distance = [4.368502806239363E+00, 4.213855691928690E+00, 3.886343576931959E+00, 3.417598266878330E+00, 2.852913125012276E+00,
2.243640928895386E+00, 1.641485782868710E+00, 1.094491537856798E+00, 6.424890386514592E-01, 3.072700467437756E-01,
9.408967194697801E-02, 1.855490327204289E-01, 3.448177055618138E-01]

dates = ['2035-Jan-01 00:00:00.0000','2035-Jan-31 08:00:00.0000','2035-Mar-02 16:00:00.0000','2035-Apr-02 00:00:00.0000',
'2035-May-02 08:00:00.0000','2035-Jun-01 16:00:00.0000','2035-Jul-02 00:00:00.0000','2035-Aug-01 08:00:00.0000',
'2035-Aug-31 16:00:00.0000','2035-Oct-01 00:00:00.0000','2035-Oct-31 08:00:00.0000','2035-Nov-30 16:00:00.0000',
'2035-Dec-31 00:00:00.0000']
dates = [pd.to_datetime(d) for d in dates]

plt.xlabel('Dates')
plt.ylabel('Distance(AU)')
plt.title('Comet 289P')

plt.plot_date(dates, distance, c = 'red')
plt.show()
