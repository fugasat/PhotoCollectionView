class Const:

    @staticmethod
    def all_type():
        return [Const.type_total(), Const.type_model(), Const.type_scene(), Const.type_angle(), Const.type_area()]

    @staticmethod
    def type_total():
        return 0

    @staticmethod
    def type_angle():
        return 1

    @staticmethod
    def type_rail():
        """
        未使用
        """
        return 2

    @staticmethod
    def type_scene():
        return 3

    @staticmethod
    def type_area():
        return 4

    @staticmethod
    def type_model():
        return 5
