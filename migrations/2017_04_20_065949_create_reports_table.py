from orator.migrations import Migration


class CreateReportsTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('reports') as table:
            table.big_increments('pk')
            table.timestamps()
            table.soft_deletes()

            table.string("title")
            table.text("report")

            table.big_integer("user_fk")
            table.foreign("user_fk").references("id").on("users")


    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('reports')
