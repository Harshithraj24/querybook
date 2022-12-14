"""Add index to admin log and impression

Revision ID: 31f9e65aef35
Revises: 7a7b02af3f1b
Create Date: 2020-05-07 17:49:50.769799

"""
from alembic import op


# revision identifiers, used by Alembic.
revision = "31f9e65aef35"
down_revision = "7a7b02af3f1b"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index(
        op.f("ix_admin_audit_log_item_id"), "admin_audit_log", ["item_id"], unique=False
    )
    op.create_index(
        op.f("ix_admin_audit_log_item_type"),
        "admin_audit_log",
        ["item_type"],
        unique=False,
    )
    op.create_index(
        op.f("ix_impression_item_id"), "impression", ["item_id"], unique=False
    )
    op.create_index(
        op.f("ix_impression_item_type"), "impression", ["item_type"], unique=False
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f("ix_impression_item_type"), table_name="impression")
    op.drop_index(op.f("ix_impression_item_id"), table_name="impression")
    op.drop_index(op.f("ix_admin_audit_log_item_type"), table_name="admin_audit_log")
    op.drop_index(op.f("ix_admin_audit_log_item_id"), table_name="admin_audit_log")
    # ### end Alembic commands ###
