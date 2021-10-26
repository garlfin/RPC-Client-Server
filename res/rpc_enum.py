from enum import Enum


class LookupKeyType(Enum):
    UnknownLookupKey = 0
    Facebook = 1
    LegacyGameCenter = 2
    Username = 3
    DeviceToken = 4
    DeviceCintaToken = 5
    GooglePlay = 6
    SCID = 7
    SignInWithApple = 8
    GameCenterTP = 9


class ReqRepType(Enum):
    UnknownReqRepType = 0
    Login = 2
    AllInOneLogin = 7
    GetClidesByFacebook = 36
    AttachFacebook = 200
    AttachGameCenter = 201
    AttachDeviceCintaToken = 204
    AttachGooglePlay = 205
    AttachSupercellId = 206
    AttachSignInWithApple = 207
    GetIdentity = 210
    AddTempLoginCode = 211
    RecoverLogin = 212
    ValidateAuthToken = 213
    LoadSupercellId = 214
    GetLoginsByLookups = 215
    GetLoginsByClides = 216
