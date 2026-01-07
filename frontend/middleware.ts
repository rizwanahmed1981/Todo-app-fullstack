import { NextRequest, NextFetchEvent } from 'next/server';
import { NextResponse } from 'next/server';

// Define which routes should be protected
const PROTECTED_ROUTES = ['/'];

export function middleware(request: NextRequest, event: NextFetchEvent) {
  const { pathname } = request.nextUrl;

  // Check if the route is protected
  const isProtectedRoute = PROTECTED_ROUTES.some(route =>
    pathname === route || pathname.startsWith(route)
  );

  // If it's a protected route, check for authentication
  if (isProtectedRoute) {
    // Check for token in cookies (server-side)
    const token = request.cookies.get('authToken')?.value;

    if (!token) {
      // Redirect to login page if not authenticated
      const url = request.nextUrl.clone();
      url.pathname = '/login';
      return NextResponse.redirect(url);
    }
  }

  // Continue with the request
  return NextResponse.next();
}

export const config = {
  matcher: [
    /*
     * Match all request paths except for the ones starting with:
     * - api (API routes)
     * - _next/static (static files)
     * - _next/image (image optimization files)
     * - favicon.ico (favicon file)
     */
    '/((?!api|_next/static|_next/image|favicon.ico).*)',
  ],
};