from sqlalchemy import Column, String, ARRAY, DECIMAL, Enum, Integer
from sqlalchemy.orm import relationship
from api.v1.models.base_model import BaseTableModel

class BillingPlan(BaseTableModel):
    __tablename__ = 'billing_plans'

    plan_name = Column(String, nullable=False)
    price = Column(DECIMAL, nullable=False)
    plan_interval = Column(
        Enum('monthly', 'yearly', 'one-off', name='plan_interval'), 
        nullable=False, 
        server_default='monthly'
    )
    currency = Column(String, nullable=False)
    features = Column(ARRAY(String), nullable=False)
    access_limit = Column(Integer, nullable=True)

    subscriptions = relationship('UserSubscription', back_populates='billing_plan')