"""add boardEditor and board as board item

Revision ID: f449a73c5838
Revises: 17f7c039ab6e
Create Date: 2022-06-15 17:37:05.219498

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = "f449a73c5838"
down_revision = "17f7c039ab6e"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column(
        "board_item",
        "board_id",
        new_column_name="parent_board_id",
        nullable=False,
        existing_type=sa.Integer(),
    )

    op.add_column("board_item", sa.Column("board_id", sa.Integer(), nullable=True))
    op.create_foreign_key(
        "board_item_board_id_fk", "board_item", "board", ["board_id"], ["id"]
    )

    op.add_column(
        "board_item",
        sa.Column("meta", sa.JSON, default={}, nullable=False),
    )

    op.create_table(
        "board_editor",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("board_id", sa.Integer(), nullable=False),
        sa.Column("uid", sa.Integer(), nullable=False),
        sa.Column("read", sa.Boolean(), nullable=False),
        sa.Column("write", sa.Boolean(), nullable=False),
        sa.ForeignKeyConstraint(
            ["board_id"],
            ["board.id"],
            name="board_editor_ibfk_1",
            ondelete="CASCADE",
        ),
        sa.ForeignKeyConstraint(
            ["uid"],
            ["user.id"],
            name="board_editor_ibfk_2",
            ondelete="CASCADE",
        ),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("board_id", "uid", name="unique_board_user"),
    )

    op.add_column(
        "board_item", sa.Column("query_execution_id", sa.Integer(), nullable=True)
    )
    op.create_foreign_key(
        "board_item_query_id_fk",
        "board_item",
        "query_execution",
        ["query_execution_id"],
        ["id"],
        ondelete="CASCADE",
    )

    op.add_column("access_request", sa.Column("board_id", sa.Integer(), nullable=True))
    op.create_foreign_key(
        "access_request_board_id_fk",
        "access_request",
        "board",
        ["board_id"],
        ["id"],
        ondelete="CASCADE",
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###

    op.drop_constraint(
        "access_request_board_id_fk", "access_request", type_="foreignkey"
    )
    op.drop_column("access_request", "board_id")

    op.drop_constraint("board_item_query_id_fk", "board_item", type_="foreignkey")
    op.drop_column("board_item", "query_execution_id")

    op.drop_table("board_editor")

    op.drop_column("board_item", "meta")

    op.drop_constraint("board_item_board_id_fk", "board_item", type_="foreignkey")
    op.drop_column("board_item", "board_id")

    op.alter_column(
        "board_item",
        "parent_board_id",
        new_column_name="board_id",
        nullable=False,
        existing_type=sa.Integer(),
    )
    # ### end Alembic commands ###
