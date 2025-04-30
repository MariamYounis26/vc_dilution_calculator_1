from model import DilutionModel
from repository import SessionRepository
from view import render_sidebar_inputs, render_results

model = DilutionModel()
repository = SessionRepository()

def main():
    pre_money, new_investment, existing_shares = render_sidebar_inputs()

    post_money = model.calculate_post_money(pre_money, new_investment)
    share_price = model.calculate_share_price(pre_money, existing_shares)
    new_shares = model.calculate_new_shares(new_investment, share_price)
    existing_pct, new_pct = model.calculate_ownership(existing_shares, new_shares)

    repository.save("calculation", {
        "pre_money": pre_money,
        "new_investment": new_investment,
        "existing_shares": existing_shares,
        "post_money": post_money
    })

    render_results(post_money, share_price, new_shares, existing_pct, new_pct)


