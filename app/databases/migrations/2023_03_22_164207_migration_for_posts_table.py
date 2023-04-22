"""MigrationForPostTable Migration."""

from masoniteorm.migrations import Migration


class MigrationForPostsTable(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("posts") as table:
            table.table_comment("Posts table")

            table.increments("id")
            table.integer("user_id").unsigned()
            table.foreign("user_id").references("id").on("users").on_delete('cascade')
            table.string("title")
            table.text("body")

            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("posts")
