"""MigrationForCommentTable Migration."""

from masoniteorm.migrations import Migration


class MigrationForCommentsTable(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("comments") as table:
            table.table_comment("Comments table")

            table.increments("id")
            table.integer("user_id").unsigned()
            table.foreign("user_id").references("id").on("users").on_delete('cascade')
            table.integer("post_id").unsigned()
            table.foreign("post_id").references("id").on("posts").on_delete('cascade')
            table.text("body")

            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("comments")
