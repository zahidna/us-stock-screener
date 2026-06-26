import os
import numpy as np
import pandas as pd
import yfinance as yf
import requests


# =========================
# CONFIG FROM GITHUB SECRETS
# =========================
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")


# =========================
# PREDEFINED TICKERS
# =========================
tickers = """
ABCL,ACAD,AAP,ACB,ACM,ACI,AFG,ADI,ADM,AIV,ADPT,ADSK,ADT,AEG,AMT,APD,ARR,BMY,AFRM,BNS,BTI,AI,CAT,AKAM,ALB,ALGN,ALL,ALLE,CL,ALNY,CMCSA,AMCR,AME,AMED,CPB,AMH,AMPL,CVS,AMWL,ANET,ANF,ANGI,ANSS,DE,DELL,DG,API,APO,APPN,APTV,ARCC,ARE,DGX,ARKO,DHR,ASAN,ASND,ASTS,ASX,ATER,ATO,AU,DNUT,AZO,BAH,BAX,BBIO,BBVA,BBY,BC,BDX,BEN,BF.B,BHP,BIIB,BILL,BIO,BIRD,EH,BMBL,EMR,ENPH,EOG,EPAM,EQIX,BNTX,EQNR,BOX,BRZE,BSX,DIA,BUD,BYND,EXPD,CAH,EXPE,CB,CCI,CCL,CDNS,CDW,CELH,CF,CG,CGC,CHD,CHRW,CHTR,CHWY,CI,EXR,CINF,FANG,FIZZ,FMC,CNC,CNI,CNQ,COF,COP,COUR,PGX,CPRI,CRL,CRON,CRSP,CRSR,CRWD,CSX,SPHD,CTSH,CUBE,CVAC,CVE,CVNA,FOXA,CZR,D,FSLR,DD,DDOG,FSLY,FTNT,GD,GDDY,GE,ACP,GFI,DKNG,DLR,DLTR,CAG,DOCN,DOV,DOW,RY,DVA,DVN,DXCM,CLX,ENTG,LEN,BMO,MRSH,VLO,AES,AGNC,ALLY,AOS,LNT,LW,GIS,ACWI,AOR,ARKK,TCPC,BLOK,BND,BNDX,BOTZ,CIBR,E,EC,ECL,GPN,GSK,EIDO,H,HAL,HCA,HES,HLF,ESS,ETSY,EXFY,HMY,HNST,HOG,HOLX,FFIV,FIGS,FIS,FIVE,FIVN,HON,HRL,HUBS,FRSH,HUM,IAC,ILMN,FUBO,FXI,INCY,GDX,ING,GILD,GLW,GPC,INO,INTU,IRM,ISRG,IT,HDV,ITW,IVZ,JBHT,JBLU,JD,JLL,JMIA,KB,ICL,ICLN,IDXX,IEF,IGOV,IIPR,KLAC,KLG,KLTR,KMX,IQ,KR,KSS,LCID,LHX,LI,IWM,LOGC,LOW,LRCX,LTC,LUV,LYB,JPIN,MAT,KD,KEYS,KGC,MCHP,MDB,MDLZ,KMB,KMI,MDT,MELI,MGM,MRVL,MSI,MT,LMND,LMT,MTB,LQD,MU,LUMN,NCLH,NDAQ,LYV,M,NEM,MBB,NET,MCK,NIO,NKE,NLY,NMR,MKC,MO,MPC,MQ,NNDM,NRDS,NTAP,NTES,NTR,NUE,NEE,NVAX,NVS,ODFL,OKTA,OTIS,PANW,PAYC,NOC,PFE,PLTR,PLUG,PSA,PSEC,PTON,PUBM,OMC,ONL,OPEN,PWR,QS,PATH,REGN,PAYO,PDBC,PGR,PHG,PHM,PLD,RELY,RIVN,PRTS,RJF,PSX,RL,RYAAY,SCCO,QQQ,SFIX,RCL,SJM,SKLZ,RENT,SNPS,SNY,SOFI,RMD,ROK,ROST,RTX,SAM,SAN,SAVA,SBSW,SPCE,SEDG,SPG,STM,SU,SKYY,SLV,SMH,SNN,SWK,SYY,TASK,TCOM,TD,SPGI,XYZ,TDOC,TEAM,TECH,SWKS,TER,TLRY,TME,TPR,TROW,TELFY,TSCO,TTE,TLT,TTWO,TWLO,TWST,TXG,TTD,UNP,UPST,UPWK,VFC,ULTA,UMC,VIPS,VMEO,VRSN,USO,UUP,VEA,VRTX,VGT,VIG,WBA,WDC,VNQ,VNQI,WIT,WIX,VTIP,VTI,VTRS,VTV,VWO,VYM,WM,WMB,WMG,WMS,WPM,WSM,WYNN,XEL,XPEV,XRAY,XLB,XLE,XLF,XLP,XLU,XLY,XYL,YUMC,Z,ZBH,ZS,ZTS,AAPL,AMZN,GOOGL,TSLA,V,XOM,UNH,COST,PG,NFLX,HD,NVO,JNJ,SAP,ASML,KO,CVX,WFC,TM,NOW,MCD,IBM,BX,BABA,AZN,MS,GPRO,INTC,AMC,BB,GT,MANU,UAA,SIRI,MSTR,LOGI,GME,MRNA,DOCU,GRAB,PINS,NOK,ZM,B,EBAY,HOOD,DB,HSY,YUM,RBLX,F,EA,DAL,UAL,BKR,CPNG,LULU,MNST,NU,SNOW,GM,BK,TGT,SE,COIN,MMM,DASH,WDAY,AON,RACE,ABNB,MCO,CMG,PYPL,SPOT,UPS,UBER,SONY,C,BA,SCHW,SHOP,UL,TXN,SHEL,ADBE,AMD,BRK.B,DBX,DLB,LEVI,EL,DUOL,DECK,CROX,BBWI,BIDU,BCS,FVRR,FNKO,GTLB,HAS,KKR,LYFT,MFC,LVS,MSCI,SNAP,TRI,TRIP,U,VALE,VSCO,WB,WEN,NVDA,META,AVGO,TSM,WMT,JPM,MA,ORCL,BAC,CRM,ABBV,MRK,ACN,CSCO,PEP,AXP,DIS,ABT,DPZ,HPE,HPQ,KHC,GRMN,OXY,AIG,FCX,HLT,USB,MAR,BLK,T,BKNG,VZ,GS,PM,GAP,NYT,PSKY,FDX,WU,STX,MTCH,MSFT,SBUX,ADP,AEP,AFL,AGCO,AMAT,AMGN,AWK,CTAS,DBO,DHI,DUK,ED,ENB,FE,HBAN,JCI,KEY,LLY,MAIN,NRG,O,PAYX,PPG,QCOM,SLB,TJX,TMUS,TSN,SATS,FOX,FUTU,ZG,AEM,ALC,BF.A,BF.B,LIN,RVTY,PUK,PRU,UA,SPLV,GLD,XLV,A,AAL,SPY
""".replace("\n", "").split(",")

tickers = list(set([t.strip() for t in tickers if t.strip()]))

# Yahoo Finance format fix
tickers = [t.replace(".", "-") for t in tickers]


# =========================
# TELEGRAM SENDER
# =========================
def send_telegram(msg):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    requests.post(url, data={
        "chat_id": CHAT_ID,
        "text": msg
    })


# =========================
# DATA
# =========================
def get_data():
    return yf.download(
        tickers=tickers,
        period="6mo",
        interval="1d",
        group_by="ticker",
        threads=True,
        progress=False
    )


# =========================
# CALC
# =========================
def calculate(df):
    df = df.copy()

    df["MA3"] = df["Close"].rolling(3).mean()
    df["MA5"] = df["Close"].rolling(5).mean()
    df["MA10"] = df["Close"].rolling(10).mean()
    df["MA20"] = df["Close"].rolling(20).mean()

    df["PrevClose"] = df["Close"].shift(1)

    df["AboveMA"] = (
        (df["Close"] > df["MA3"]) &
        (df["Close"] > df["MA5"]) &
        (df["Close"] > df["MA10"]) &
        (df["Close"] > df["MA20"])
    )

    df["DistanceMA20"] = (df["Close"] - df["MA20"]) / df["MA20"] * 100

    df["BUY_SETUP"] = df["AboveMA"] & (df["DistanceMA20"] <= 5)

    df["VolumeMA20"] = df["Volume"].rolling(20).mean()
    df["VolumeRatio"] = df["Volume"] / df["VolumeMA20"]

    high_low = df["High"] - df["Low"]
    high_close = (df["High"] - df["Close"].shift(1)).abs()
    low_close = (df["Low"] - df["Close"].shift(1)).abs()

    tr = pd.concat([high_low, high_close, low_close], axis=1).max(axis=1)
    df["ATR14"] = tr.rolling(14).mean()

    return df


# =========================
# FORMAT
# =========================
def fmt_ma(price, ma):
    if np.isnan(ma):
        return "N/A"
    diff = (ma - price) / price * 100
    emoji = "🟢" if diff <= 0 else "🔴"
    return f"{ma:.2f} ({emoji}{diff:+.2f}%)"


def run():
    data = get_data()

    results = []

    for ticker in tickers:
        try:
            df = data[ticker].dropna()
            if len(df) < 30:
                continue

            df = calculate(df)
            last = df.iloc[-1]

            if not bool(last["BUY_SETUP"]):
                continue

            price = float(last["Close"])
            high = float(last["High"])
            low = float(last["Low"])
            prev = float(last["PrevClose"])

            change = (price - prev) / prev * 100
            emoji = "🟢" if change >= 0 else "🔴"

            atr = float(last["ATR14"])

            # TP logic
            tp1 = price + atr
            tp2 = price + 2 * atr

            results.append(f"""
📈 {ticker}
═══════════════

💰 Close: {emoji} {price:.2f} ({change:+.2f}%)
High: {high:.2f} | Low: {low:.2f}

📉 Trend
MA3  : {fmt_ma(price,last['MA3'])}
MA5  : {fmt_ma(price,last['MA5'])}
MA10 : {fmt_ma(price,last['MA10'])}
MA20 : {fmt_ma(price,last['MA20'])}

🎯 TP
TP1: {tp1:.2f}
TP2: {tp2:.2f}

━━━━━━━━━━━━━━━
""")

        except:
            continue

    if not results:
        send_telegram("No signal today.")
        return

    final_msg = "\n".join(results[:10])
    send_telegram(final_msg)


if __name__ == "__main__":
    run()