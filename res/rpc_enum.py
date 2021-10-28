from enum import Enum


class ErrorKeyType(Enum):
    """"Errors from the server"""
    notFound = 0
    unknown = 1
    noAccount = 2
    serverError = 3
    otherError = 4


errorSyn = {
    ErrorKeyType.notFound: "[ERROR] Stats not found",
    ErrorKeyType.unknown: "[ERROR] Unknown error",
    ErrorKeyType.noAccount: "[ERROR] Account not found",
    ErrorKeyType.serverError: "[ERROR] Server error",
    ErrorKeyType.otherError: "[ERROR] Not specified"
}


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
