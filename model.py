# vc_dilution_calculator/model/dilution_model.py
class DilutionModel:
    """Model for VC ownership dilution calculations."""

    @staticmethod
    def calculate_post_money(pre_money: float, new_investment: float) -> float:
        return pre_money + new_investment

    @staticmethod
    def calculate_share_price(pre_money: float, existing_shares: int) -> float:
        return pre_money / existing_shares

    @staticmethod
    def calculate_new_shares(new_investment: float, share_price: float) -> float:
        return new_investment / share_price

    @staticmethod
    def calculate_ownership(existing_shares: int, new_shares: float) -> tuple:
        total_shares = existing_shares + new_shares
        existing_pct = (existing_shares / total_shares) * 100
        new_pct = (new_shares / total_shares) * 100
        return existing_pct, new_pct

