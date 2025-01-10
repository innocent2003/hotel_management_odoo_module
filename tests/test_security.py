from odoo.tests import TransactionCase

class TestSecurity(TransactionCase):
    def test_access_control(self):
        # Create a sample room
        room = self.env['session7.hotel.room'].create({
            'name': 'Room 101',
            'price': 100.0,
            'is_available': True,
        })

        # Test Manager Access
        manager_group = self.env.ref('base.group_user')
        self.env.user.groups_id |= manager_group
        room.sudo(self.env.user).write({'price': 150.0})

        # Test Staff Access
        self.env.user.groups_id -= manager_group
        with self.assertRaises(Exception):
            room.sudo(self.env.user).write({'price': 200.0})
