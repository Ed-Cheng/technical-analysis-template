tickers = ["nvda", "amzn"]

for ticker in tickers:
    data = yf.download(ticker, period="200d", interval="1d", progress=False)

    fig = go.Figure(
        data=[
            go.Candlestick(
                x=data.index,
                open=data["Open"],
                high=data["High"],
                low=data["Low"],
                close=data["Close"],
            )
        ]
    )

    fig.add_trace(
        go.Scatter(
            x=data.index,
            y=data["Close"].rolling(window=5).mean(),
            mode="lines",
            name="5ma",
            marker_color="green",
            opacity=0.7,
        )
    )

    # Update the layout
    fig.update_layout(
        title="Sample Candlestick Chart",
        yaxis_title="Stock Price",
        xaxis_title="Date",
        height=600,
        xaxis_rangeslider_visible=False,
        margin=dict(l=0, r=10, t=30, b=30),
    )

    # Show the figure
    fig.show()
