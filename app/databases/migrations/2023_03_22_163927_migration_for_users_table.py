"""MigrationForUserTable Migration."""

from masoniteorm.migrations import Migration


class MigrationForUsersTable(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("users") as table:
            table.table_comment("Users table")

            table.increments("id")
            table.string("name")
            table.string("email").unique()
            table.string("address").nullable()
            table.string("phone_number", 11).nullable()
            table.enum("sex", ["female", "male"]).nullable()
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("users")
