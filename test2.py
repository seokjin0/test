def damage_avg(df):
    df = match_df[['CHAMPIONNAME', 'TOTALDAMAGEDEALTTOCHAMPIONS', 'TOTALDAMAGETAKEN']]
    df2 = df.groupby(['CHAMPIONNAME']).mean()
    df3 = df2.rename(columns={'TOTALDAMAGEDEALTTOCHAMPIONS': '평균 가한 데미지', 'TOTALDAMAGETAKEN': '평균 받은 데미지'})
    df3 = df3.reset_index()

    from matplotlib import font_manager, rc
    font_path = 'C:/Windows/Fonts/gulim.ttc'
    font = font_manager.FontProperties(fname=font_path).get_name()
    rc('font', family=font)
    fig = px.scatter(df3, x='평균 가한 데미지', y='평균 받은 데미지',
                     hover_data=['CHAMPIONNAME'],
                     title='강석진_라인별 15분 골드 그래프')
    fig.show()