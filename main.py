def main_app():
    # --- LOGOUT BUTTON ---
    col1, col2 = st.columns([6, 1])
    with col2:
        if st.button("🚪 Logout"):
            st.session_state.logged_in = False
            st.rerun()

    # --- STYLES ---
    st.markdown("""
        <style>
            body, .stApp {
                background-color: #f9f9f9;
                font-family: 'Helvetica Neue', sans-serif;
            }
            .portfolio-header {
                font-size: 28px;
                font-weight: 700;
                margin-bottom: 5px;
            }
            .owner-name {
                font-size: 16px;
                font-weight: 400;
                color: #666;
                margin-bottom: 10px;
            }
            .value-box {
                font-size: 36px;
                font-weight: 700;
            }
            .small-green {
                color: green;
                font-size: 14px;
            }
            .small-red {
                color: red;
                font-size: 14px;
            }
        </style>
    """, unsafe_allow_html=True)

    # --- STATIC DATA ---
    owner_name = "Steven Etcheverry"
    wallet_address = "18zW9ngXygR4BmNHk8vFVzybAUq7Y9LVkY"
    portfolio_value = 900182.99
    btc_price = 107716.04
    btc_holdings = round(portfolio_value / btc_price, 6)
    gain_24h = 900182.99
    gain_all_time = 246.75
    change_percent = "+0.02%"
    btc_change = "-2.38%"

    # --- HEADER ---
    st.markdown(f"<div class='portfolio-header'>Portfolio 1</div>", unsafe_allow_html=True)
    st.markdown(f"<div class='owner-name'>Wallet Owner: {owner_name}</div>", unsafe_allow_html=True)
    st.markdown(f"<div class='value-box'>${portfolio_value:,.2f}</div>", unsafe_allow_html=True)
    st.markdown(f"<div class='small-green'>24h: +${gain_24h:,.2f} --</div>", unsafe_allow_html=True)
    st.markdown(f"<div class='small-green'>All-time: +${gain_all_time:.2f} ▲ {change_percent}</div>", unsafe_allow_html=True)

    # --- TABS ---
    tab1, tab2, tab3 = st.tabs(["Overview", "Transactions", "Send BTC"])

    # --- OVERVIEW TAB ---
    with tab1:
        st.subheader("Holdings")
        st.line_chart([random.uniform(895000, 902000) for _ in range(10)])

        st.markdown("### BTC")
        col1, col2 = st.columns([1, 2])
        col1.image("https://cryptologos.cc/logos/bitcoin-btc-logo.png", width=35)
        col2.write(f"Price: ${btc_price:,.2f}  \nHoldings: ${portfolio_value:,.2f} ({btc_holdings} BTC)  \nChange: {btc_change}")

    # --- TRANSACTIONS TAB ---
    with tab2:
        st.subheader("📄 Recent Transactions")
        transactions = [
            {
                "type": "Received",
                "amount": btc_holdings,
                "date": "2025-05-30 10:00:00",
                "description": "Publishers Clearing House",
                "status": "Confirmed"
            }
        ]

        for i in range(5):
            transactions.append({
                "type": random.choice(["Sent", "Received"]),
                "amount": round(random.uniform(0.01, 0.15), 6),
                "date": (datetime.datetime.now() - datetime.timedelta(days=i+1)).strftime("%Y-%m-%d %H:%M:%S"),
                "description": "",
                "status": random.choice(["Pending", "Confirmed"])
            })

        for tx in transactions:
            st.markdown(f"""
            **{tx['type']}** | `{tx['date']}`  
            Amount: `{tx['amount']} BTC`  
            Status: **{tx['status']}**  
            {f"📝 Description: {tx['description']}" if tx['description'] else ""}
            ---
            """)

    # --- SEND BTC TAB ---
    with tab3:
        st.subheader("📤 Send Bitcoin")

        with st.form("send_btc_form"):
            recipient = st.text_input("Recipient BTC Address")
            amount_to_send = st.number_input("Amount to Send (BTC)", min_value=0.0001, max_value=btc_holdings)
            token = st.text_input("🔐 Enter 6-digit Token Code", max_chars=6)
            submitted = st.form_submit_button("Send")

            if submitted:
                if not recipient or not token:
                    st.error("❌ Please fill in all fields.")
                elif len(token) != 6 or not token.isdigit():
                    st.error("❌ Invalid token code.")
                elif amount_to_send > btc_holdings:
                    st.error("❌ Amount exceeds wallet balance.")
                else:
                    st.success(f"✅ {amount_to_send} BTC sent to `{recipient}` (Token verified).")
